# How to Downlaod Any PDF file with JS?
```html

<a href="sample.pdf" download>
    <button>Download PDF</button>
</a>

<button onclick="downloadPDF()">Download PDF</button>

<script>
function downloadPDF() {
    const link = document.createElement("a");
    link.href = "sample.pdf";  
    link.download = "MyFile.pdf"; 
    link.click();
}
</script>
```