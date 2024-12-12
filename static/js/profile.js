// let input = document.querySelectorAll('.add-car .inner-container input')
// let label = document.querySelectorAll('.add-car .inner-container label')
// let form = document.querySelector('.add-car form')
// let errorMessage = document.querySelector('.error')

// let input_2 = document.querySelectorAll('.user-update-form input')
// let label_2 = document.querySelectorAll('.user-update-form label')

// let textarea = document.querySelectorAll('.add-car .bottom textarea')
// let label2 = document.querySelectorAll('.add-car .bottom label')

// handleInput(input, label)
// handleInput(input_2, label_2)
// handleTextArea(textarea, label2)

// function handleInput(Input, Label){
// 	Input.forEach((el, index) => {
// 		const handleLabel = (e) => {
// 			Label.forEach((lv, ix) => {
// 				lv.style.top = '28px'
// 				lv.style.fontSize = '15px'
// 				if(Input[ix].value !== ''){
// 					lv.style.top = '10px'
// 					lv.style.fontSize = '10px'
// 				}
// 			})
// 			if(e.type == 'focusin'){
// 				Label[index].style.top = '10px'
// 				Label[index].style.fontSize = '10px'
// 			}
// 		}
// 		el.addEventListener('focusin', handleLabel)
// 		el.addEventListener('focusout', handleLabel)
// 	})
// }
// function handleTextArea(Input, Label){
// 	Input.forEach((el, index) => {
// 		const handleLabel = (e) => {
// 			Label.forEach((lv, ix) => {
// 				lv.style.top = '28px'
// 				lv.style.fontSize = '15px'
// 				if(Input[ix].innerText !== ''){
// 					lv.style.top = '10px'
// 					lv.style.fontSize = '10px'
// 				}
// 			})
// 			if(e.type == 'focusin'){
// 				Label[index].style.top = '10px'
// 				Label[index].style.fontSize = '10px'
// 			}
// 		}
// 		el.addEventListener('focusin', handleLabel)
// 		el.addEventListener('focusout', handleLabel)
// 	})
// }

// // Adding Car | form submit
// form.addEventListener('submit', addCarSubmit)

// async function addCarSubmit(e) {
//     e.preventDefault();
//     let formData = new FormData(e.target); // Get the form that triggered the event
//     console.log(Array.from(formData));

//     let loader = document.querySelector('.loading');
//     let btn_text = document.querySelector('.button-text');

//     loader.classList.remove('hide');
//     btn_text.classList.add('hide');

//     let url = '/user/add-car/';
//     try {
//         const res = await fetch(url, {
//             method: "POST",
//             body: formData
//         });

//         if (!res.ok) {
//             throw new Error('Network response was not ok');
//         }

//         const data = await res.json();
//         console.log(data);
        
//         // Reload the page after successful addition
//         window.location.reload();
        
//         loader.classList.add('hide');
//         btn_text.classList.remove('hide');
//     } catch (err) {
//         console.error(err);
//         loader.classList.add('hide');
//         btn_text.classList.remove('hide');
//     }
// }



let input = document.querySelectorAll('.add-car .inner-container input')
let label = document.querySelectorAll('.add-car .inner-container label')
let form = document.querySelector('.add-car form')
let errorMessage = document.querySelector('.error')

let input_2 = document.querySelectorAll('.user-update-form input')
let label_2 = document.querySelectorAll('.user-update-form label')

let textarea = document.querySelectorAll('.add-car .bottom textarea')
let label2 = document.querySelectorAll('.add-car .bottom label')

handleInput(input, label)
handleInput(input_2, label_2)
handleTextArea(textarea, label2)

function handleInput(Input, Label){
    Input.forEach((el, index) => {
        const handleLabel = (e) => {
            Label.forEach((lv, ix) => {
                lv.style.top = '28px'
                lv.style.fontSize = '15px'
                if(Input[ix].value !== ''){
                    lv.style.top = '10px'
                    lv.style.fontSize = '10px'
                }
            })
            if(e.type == 'focusin'){
                Label[index].style.top = '10px'
                Label[index].style.fontSize = '10px'
            }
        }
        el.addEventListener('focusin', handleLabel)
        el.addEventListener('focusout', handleLabel)
    })
}

function handleTextArea(Input, Label){
    Input.forEach((el, index) => {
        const handleLabel = (e) => {
            Label.forEach((lv, ix) => {
                lv.style.top = '28px'
                lv.style.fontSize = '15px'
                if(Input[ix].value !== ''){
                    lv.style.top = '10px'
                    lv.style.fontSize = '10px'
                }
            })
            if(e.type == 'focusin'){
                Label[index].style.top = '10px'
                Label[index].style.fontSize = '10px'
            }
        }
        el.addEventListener('focusin', handleLabel)
        el.addEventListener('focusout', handleLabel)
    })
}

// Adding Car | form submit
form.addEventListener('submit', addCarSubmit)

async function addCarSubmit(e) {
    e.preventDefault();
    let formData = new FormData(e.target); // Get the form that triggered the event
    console.log(Array.from(formData));
	console.log('mk');

    let loader = document.querySelector('.loading');
    let btn_text = document.querySelector('.button-text');

    loader.classList.remove('hide');
    btn_text.classList.add('hide');

    let url = '/user/add-car/'; // Update with the correct URL if necessary
    try {
        const res = await fetch(url, {
            method: "POST",
            body: formData
        });

        if (!res.ok) {
            throw new Error('Network response was not ok');
        }

        const data = await res.json();
        console.log(data);

		console.log('mk');
        
        // Reload the page after successful addition
        window.location.reload();
        
    } catch (err) {
        console.error(err);
    } finally {
        loader.classList.add('hide');
        btn_text.classList.remove('hide');
    }
}


