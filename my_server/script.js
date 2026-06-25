const body = document.body;
const sidebarToggleBtn = document.getElementById('sidebar-toggle-btn');
const openFloatingBtn = document.getElementById('open-sidebar-floating');
const mobileHamburger = document.getElementById('mobile-hamburger');

function toggleSidebar() {
    body.classList.toggle('sidebar-collapsed');
    const isCollapsed = body.classList.contains('sidebar-collapsed');
    localStorage.setItem('sidebar-collapsed', isCollapsed ? 'true' : 'false');
}

// Restore previous state
const savedState = localStorage.getItem('sidebar-collapsed');
// On mobile, default should be collapsed (hidden). On desktop, respect saved state.
const isMobile = window.matchMedia('(max-width: 768px)').matches;
if (isMobile) {
    // On mobile, always start collapsed (sidebar hidden)
    body.classList.add('sidebar-collapsed');
} else {
    if (savedState === 'true') {
        body.classList.add('sidebar-collapsed');
    } else {
        body.classList.remove('sidebar-collapsed');
    }
}

sidebarToggleBtn.addEventListener('click', toggleSidebar);
openFloatingBtn.addEventListener('click', toggleSidebar);
mobileHamburger.addEventListener('click', toggleSidebar);

// Keyboard shortcut
document.addEventListener('keydown', (e) => {
    if ((e.ctrlKey || e.metaKey) && (e.key === 'b' || e.key === '\\')) {
        e.preventDefault();
        toggleSidebar();
    }
});

// Also close sidebar on mobile when clicking outside (optional)
document.addEventListener('click', (e) => {
    if (isMobile && !body.classList.contains('sidebar-collapsed')) {
        const sidebar = document.getElementById('sidebar');
        if (!sidebar.contains(e.target) && e.target !== mobileHamburger) {
            body.classList.add('sidebar-collapsed');
        }
    }
});

// ========== File tree & Markdown logic (unchanged) ==========
let currentActive = null;

async function loadFileTree() {
    const res = await fetch('/api/files');
    const files = await res.json();
    const container = document.getElementById('file-tree-container');

    if (files.length === 0) {
        container.innerHTML = '<p style="color:#585b70;">Koi .md file nahi mili</p>';
        return;
    }

    const tree = {};
    files.forEach(path => {
        const parts = path.split('/');
        let current = tree;
        for (let i = 0; i < parts.length - 1; i++) {
            const folder = parts[i];
            if (!current[folder]) current[folder] = { __files: [] };
            current = current[folder];
        }
        const file = parts[parts.length - 1];
        current.__files = current.__files || [];
        current.__files.push({ name: file, fullPath: path });
    });

    function renderTree(node) {
        const folders = Object.keys(node).filter(k => k !== '__files').sort();
        const files = (node.__files || []).sort((a, b) => a.name.localeCompare(b.name));
        let html = '<ul class="file-tree">';
        folders.forEach(folder => {
            html += `
            <li class="folder-item">
              <div class="folder-header" onclick="toggleFolder(this)">
                <span class="folder-arrow">▶</span>
                <span class="folder-icon">📁</span>
                <span>${folder}</span>
              </div>
              <div class="folder-children">
                ${renderTree(node[folder])}
              </div>
            </li>
          `;
        });
        files.forEach(file => {
            html += `
            <li>
              <span class="file-item" data-path="${file.fullPath.replace(/"/g, '&quot;')}" onclick="openFile(this, '${file.fullPath.replace(/'/g, "\\'")}')">
                📄 ${file.name}
              </span>
            </li>
          `;
        });
        html += '</ul>';
        return html;
    }
    container.innerHTML = renderTree(tree);
}

function toggleFolder(header) {
    const childrenDiv = header.nextElementSibling;
    const arrow = header.querySelector('.folder-arrow');
    if (childrenDiv.classList.contains('open')) {
        childrenDiv.classList.remove('open');
        arrow.classList.remove('open');
        arrow.textContent = '▶';
    } else {
        childrenDiv.classList.add('open');
        arrow.classList.add('open');
        arrow.textContent = '▼';
    }
}

async function openFile(element, path) {
    if (currentActive) currentActive.classList.remove('active');
    element.classList.add('active');
    currentActive = element;

    const res = await fetch(`/api/file?path=${encodeURIComponent(path)}`);
    if (!res.ok) {
        document.getElementById('markdown-content').innerHTML = '<p class="empty-msg">File load karne mein error</p>';
        return;
    }
    const mdText = await res.text();
    const html = marked.parse(mdText);
    document.getElementById('markdown-content').innerHTML = html;

    document.querySelectorAll('.markdown-body pre code').forEach((block) => {
        hljs.highlightElement(block);
    });

    // On mobile, after selecting a file, auto-close sidebar
    if (window.innerWidth <= 768) {
        body.classList.add('sidebar-collapsed');
    }
}

loadFileTree();