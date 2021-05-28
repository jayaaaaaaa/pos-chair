let url = 'https://api.thingspeak.com/channels/1401991/fields/1/last.json';

window.onload = fetchJson()

setInterval(function(){ 
    fetchJson()    
}, 5000);

function fetchJson() {
    fetch(url)
    .then(res => res.json())
    .then((out) => {
    DisplayResults(out);    
    })
    .catch(err => { throw err });
}

function DisplayResults(data) {
    DisplayPosture(data.field1);
    const displayDate = document.getElementById("date");
    const event = new Date(data.created_at);
    const options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' };
    const showResult = event.toLocaleDateString('en-NZ', options);
    displayDate.innerHTML = showResult; 
  }

function DisplayPosture(output) {
    let text = ' ';
    const postureResult = document.getElementById("posture");
    switch(output) {
        case '0':
            text = "Correct Posture"
            ChangeToGreen();
            break;
        case '1':
            text = "Are you slouching?"
            ChangeToRed();
            break;
        case '2':
            text = "You may be leaning forward."
            ChangeToRed();
            break;
        case '3':
            text = "A little bit imbalanced. You may be leaning on your left side."
            ChangeToRed();
            break;
        case '4':
            text = "Are you leaning on your right? Try sitting with your weight equal on both sides."
            ChangeToRed();
            break;
        default:
            text = "Waiting for posture information..."
            ChangeToGreen();
            break;
    }
    postureResult.innerHTML = text; 
    }

function ChangeToRed() {
    document.body.style.backgroundImage = "url('bad.svg')";
}

function ChangeToGreen() {
    document.body.style.backgroundImage = "url('good.svg')";
}
