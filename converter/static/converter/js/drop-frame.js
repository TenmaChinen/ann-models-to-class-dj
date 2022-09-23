PATTERN_ALLOWED_FORMATS = "h5|json";

class DragDropFile {
  constructor(elementId) {
    this.dropFrame = document.getElementById(elementId);
    this.initContent();
    this.dropCallback = null;
  }

  initContent(){
    this.dropFrame.innerHTML += `<div class="drop-overlay">Drop your files<br>to convert them</div>` ;
    this.dropFrame.innerHTML += `<div class="drop-content"></div>` ;
    
    this.dropOverlay = this.dropFrame.querySelector(".drop-overlay");
    this.dropContent = this.dropFrame.querySelector(".drop-content");
    
    this.dropOverlay.addEventListener("drop", this);
    this.dropFrame.addEventListener("dragover", this);
    this.dropOverlay.addEventListener("dragleave", this);
  }

  setDropCallback(callback) {
    this.dropCallback = callback;
  }

  onDragOver(event) {
    this.showDropOverlay();
    event.stopPropagation();
    event.preventDefault();
    event.dataTransfer.dropEffect = "copy";
  }

  onDragLeave(event) {
    this.hideDropOverlay();
    event.stopPropagation();
    event.preventDefault();
  }

  showDropOverlay() {
    this.dropOverlay.classList.add("show");
  }

  hideDropOverlay() {
    this.dropOverlay.classList.remove("show");
  }

  onDrop(event) {
    event.stopPropagation();
    event.preventDefault();
    this.hideDropOverlay();
    const files = event.dataTransfer.files;
    let fileReader,fileFormat;
    
    for (let idx = 0, file; idx < files.length; idx++) {
      file = files[idx];
      fileFormat = file.name.split(".").at(-1);

      if (fileFormat.match(PATTERN_ALLOWED_FORMATS)) {

        this.dropCallback(file,fileFormat);
        // fileReader = new FileReader();
        // fileReader.fileFormat = fileFormat;
        // fileReader.fileName = file.name;
        // fileReader.addEventListener("load", this);
        // fileReader.readAsDataURL(file);
      }
    }
  }

  onFileLoaded(event) {
    if (this.dropCallback) {
      const fileReader = event.target;
      const fileFormat = fileReader.fileFormat;
      const fileName = fileReader.fileName;
      const fileData = fileReader.result;
      this.dropCallback(fileName,fileFormat,fileData);
    }
  }

  handleEvent(event) {
    // console.log(e.type);
    switch (event.type) {
      case "drop":
        this.onDrop(event);
        break;
      case "dragover":
        this.onDragOver(event);
        break;
      case "dragleave":
        this.onDragLeave(event);
        break;
      case "load":
        this.onFileLoaded(event);
    }
  }

}
