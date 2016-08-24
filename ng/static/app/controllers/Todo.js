app.controller("TodoCtrl", function($scope) {

  $scope.title = "Welcome to Angular";
  $scope.macaroni = "";
  $scope.newTodo = "";

  $scope.todos = [
    { name: "Make lunches", type: "home" },
    { name: "Install closet shelves", type: "home" },
    { name: "Mow the lawn", type: "home" },
    { name: "Cut the grass", type: "home" },
    { name: "Install microservice observer", type: "work" },
    { name: "Schedule weekly scrum", type: "work" }
  ];

  $scope.killTodo = function(todo) {
    var todoIndex = $scope.todos.indexOf(todo);
    if (todoIndex >= 0) {
      $scope.todos.splice(todoIndex, 1);
    }
  };

  $scope.addTodo = function() {
    $scope.todos.push({name: $scope.newTodo, type: "home"});
    $scope.newTodo = "";
  };

});