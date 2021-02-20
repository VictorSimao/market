const ciaTr = document.querySelector("table[name=salesman]")

fetch("http://localhost:5000/salesman")
.then( res  => res.json() )
.then( company => {
    
    for( const data of company ) {
        ciaTr.innerHTML += `<tr><td>${data[1]}</td><td>${data[4]}</td></tr>`
    }

} )

function populatesCias() {
    const ciaSelect = document.querySelector("select[name=salesman]")

    fetch("http://localhost:5000/salesman")
    .then( res  => res.json() )
    .then( company => {
        
        for( const data of company ) {
            ciaSelect.innerHTML += `<option value="${data[0]}">${data[1]}</option>`
        }
 
    } )
}

populatesCias()