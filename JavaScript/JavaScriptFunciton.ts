// Function Declaration
function myFunction() {
  console.log("Function Declaration");
}

// Function Expression
const myFunctionExpression = function (a, b) {
  console.log("Function Expression");
};

// Arrow Function
const myArrowFunction = () => {
  console.log("Arrow Function");
};

// Method in an Object
const myObject = {
  myMethod: function () {
    console.log("Method in an Object");
  },
};

// ES6 Method Definition in an Object
const myObjectES6 = {
  myMethod() {
    console.log("ES6 Method Definition in an Object");
  },
};

// Call each function
myFunction();
let a = 2,
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
const myInstance = new MyConstructor();
myInstance.myMethod();
