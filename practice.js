let username = "subhash";
let email = "abc@gmail.com";
let contact = 09876;

// I want to send these details to remote application/code.
// I know that we have to do serialisation before sending data.

// JSON !
let data = {
    name_value : username,
    email_value : email,
    contact_value : contact
}

console.log("***************************************SERIALISATION**************************");

console.log("Before Stringify:");
console.log(data);
console.log(typeof(data))

console.log("After stringify: ");

stringify_data = JSON.stringify(data);

console.log(stringify_data);
console.log(typeof(stringify_data));

console.log("***************************************DE-SERIALISATION**************************");

json_data = JSON.parse(stringify_data);
console.log(json_data);


