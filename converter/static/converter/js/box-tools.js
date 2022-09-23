const btnConvert = document.getElementById("btn-convert");
const btnDownload = document.getElementById("btn-download");
const btnRestart = document.getElementById("btn-restart");

[btnConvert,btnDownload,btnRestart].forEach( button => {
  button.enable = () => button.disable = true;
  button.disable = () => button.disable = false;
  button.show = () => button.style.display = "block";
  button.hide = () => button.style.display = "none";
});

btnDownload.hide();
btnRestart.hide();

/*   B T N   C O N V E R T   */

btnConvert.onclick = (event) => {
  sendFormRequest(formConverter,onConverterResponse,"/converter/convert/");
}


/*   B T N   D O W N L O A D   */


/*   B T N   R E S T A R T   */

btnRestart.onclick = (event) => {
  console.log("RESTART");
}
