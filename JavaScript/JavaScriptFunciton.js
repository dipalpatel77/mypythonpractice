// Function Declaration
function myFunction() {
  console.log("Function Declaration");
}
// Function Expression
var myFunctionExpression = function (a, b) {
  console.log(a + b + " = Function Expression = " + a + b);
};
// Arrow Function
var myArrowFunction = function () {
  console.log("Arrow Function");
};
// Method in an Object
var myObject = {
  myMethod: function () {
    console.log("Method in an Object");
  },
};
// ES6 Method Definition in an Object
var myObjectES6 = {
  myMethod: function () {
    console.log("ES6 Method Definition in an Object");
  },
};
// Call each function
myFunction();
var a = 2,
  b = 3;
myFunctionExpression(a, b);
myArrowFunction();
myObject.myMethod();
myObjectES6.myMethod();
function MyConstructor() {
  this.myMethod = function () {
    console.log("Constructor Function");
  };
}
// Immediately Invoked Function Expression (IIFE)
(function () {
  console.log("Immediately Invoked Function Expression (IIFE)");
})();
(function () {
  console.log("This is the first Immediately Invoked funciton");
})();
// Constructor Function
var myInstance = new MyConstructor();
myInstance.myMethod();

const result = (function (a, b) {
  return a + b;
})(a, b);

console.log("result == " + result); // Output: 10

// Generator Function
function* myGeneratorFunction() {
  console.log("Generator Function");
  yield "First Yield";
  yield "Second Yield";
}
const generator = myGeneratorFunction();
console.log(generator.next().value);
console.log(generator.next().value);

// Async Function
async function myAsyncFunction() {
  console.log("Async Function");
  return "Async Result";
}
myAsyncFunction().then((result) => console.log(result));
