class BoxFile{
  constructor(elementId){
    this.parent = document.getElementById(elementId);
    this.tickIcon = this.parent.querySelector(".tick-icon");
    this.fileName = this.parent.querySelector(".file-name")
  }

  setLoadVisibility(state){
    this.tickIcon.style.display = state ? "block" : "none" ;
    this.fileName.style.display = state ? "block" : "none" ;
  }

  setFileName(fileName){
    this.fileName.innerHTML = fileName;
  }
}