/**
 * Created by adria on 5/15/2017.
 */

// int 12015
// float 5098.098
// list/array []
// string 'tis a string'
// json {'key': 'value',}
//
// variables always start with var

var name = [
    'chris',
    'katie',
    'chelsea'
];

function greet(n) {
    var color;
    if (n === 'Loopersan') {
        color = '#3732e0'
    } else if (n === 'Mike') {
        color = '#E0200D'
    } else {
        color = '#24e016'
    }
    var message = document.getElementById('message');
        message.innerHTML = 'Hello ' + n + '!';
        message.style.color = color;
}

// for (var i = 0; i < names.length; i++) {
//     console.log(greet(name[i]));
// }
//
// var button = document.getElementById('getName');

document.getElementById('getName').addEventListener('click', function() {
    var name = document.getElementById('name').value;
    console.log(greet(name));
});

// console.log(greet(document.getElementById('name').value)));