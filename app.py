import math
import time
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

MAX_ITERATIONS = 200


@app.route("/")
def index():
    # Renders the main user interface
    return render_template("index.html")


@app.route("/run_benchmark", methods=["POST"])
def run_benchmark():
    data = request.get_json() or {}
    iterations_raw = data.get("iterations", "20")

    # Validation mirroring your desktop app logic
    if (
        not iterations_raw.isdigit()
        or int(iterations_raw) < 20
        or int(iterations_raw) > MAX_ITERATIONS
    ):
        return (
            jsonify({"error": "Please enter a valid number of iterations (20-200)."}),
            400,
        )

    iterations = int(iterations_raw)

    # Benchmark Logic
    start_time = time.time()
    for _ in range(iterations):
        result = 0
        for i in range(1, 1000000):
            result += math.sqrt(i)
    end_time = time.time()

    elapsed_time = end_time - start_time
    elapsed_time_ms = elapsed_time * 1000

    # Scoring mechanism
    score = 100 / elapsed_time if elapsed_time > 0 else 0

    return jsonify(
        {
            "score": f"{score:.2f} out of 100",
            "time_ms": f"{elapsed_time_ms:.2f} ms",
        }
    )


if __name__ == "__main__":
    app.run(debug=True)
