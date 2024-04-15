function runPythonFunction() {
    eel.run_python_code()(function(response) {
        document.getElementById('pythonResponse').innerHTML = response;
    });
}

