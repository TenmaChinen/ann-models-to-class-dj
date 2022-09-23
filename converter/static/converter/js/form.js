const formConverter = document.getElementById("form-converter");

function setFormFileJson(file){
  formConverter.fileJson.files = fileToFiles(file);
}

function setFormFileH5(file){
  formConverter.fileH5.files = fileToFiles(file);
}

function fileToFiles(file){
  const dataTransfer = new DataTransfer();
  dataTransfer.items.add(file);
  return dataTransfer.files;
}