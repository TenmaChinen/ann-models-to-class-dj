/*
  text/plain
  text/x-python
  text/javascript
  text/css  
*/

dataTypes = {
  0 : "py",
  1 : "js"
}

function setDownloadContent(text, name = "model", fmt = "py") {
  const encodedContent = encodeURIComponent(text);
  const dataType = `text/plain`;
  const encodeType = "charset=utf-8";
  const fileName = `${name}.${fmt}`;

  btnDownload.setAttribute("href", `data:${dataType};${encodeType},${encodedContent}`);
  btnDownload.setAttribute("download", fileName);
}