# How to Integrate Map in Html?

```html
 <h1>Our Location</h1>
<!-- Google Map -->
<iframe
      src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3620.123456!2d67.123456!3d24.123456!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3eb33e456789abcdef%3A0x123456789abcdef!2sKarachi!5e0!3m2!1sen!2s!4v1234567890"
      width="800"
      height="600"
      style="border:0;"
      allowfullscreen=""
      loading="lazy">
</iframe>
```

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