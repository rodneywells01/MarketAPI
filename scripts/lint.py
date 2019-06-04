from pylint import epylint

PASSINGSCORE = 7.0

# Execute pylint test.
pylint_out, pylint_stderr = epylint.py_run("marketAPI", return_std=True)
results = pylint_out.getvalue()
if pylint_stderr.getvalue():
    raise Exception(f"Error evaluating pylint: {pylint_stderr.getvalue()}")
print(results)

# Extract the score with string manipulation (I can't belive pylint doesn't support this better)
searchkey = "code has been rated at "
res_idx_start = results.rfind(searchkey) + len(searchkey)
res_idx_end = results[res_idx_start:].find("/")
score = float(results[res_idx_start : res_idx_start + res_idx_end])
print(f"Pylint score of {score}")

# Evaluate Pass Fail
if score < PASSINGSCORE:
    raise Exception(f"FAILURE TO PASS Pylint - {score} < {PASSINGSCORE}")
