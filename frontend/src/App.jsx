import { useMemo, useState } from "react";

const API_BASE = import.meta.env.VITE_API_BASE ?? "http://127.0.0.1:8000";

const regions = ["northeast", "northwest", "southeast", "southwest"];
const sexes = ["male", "female"];
const smokerOptions = ["yes", "no"];

function classNames(...xs) {
  return xs.filter(Boolean).join(" ");
}

function formatCurrency(n) {
  if (Number.isNaN(n)) return "";
  return new Intl.NumberFormat(undefined, {
    style: "currency",
    currency: "USD",
    maximumFractionDigits: 0,
  }).format(n);
}

export default function App() {
  const [form, setForm] = useState({
    age: 31,
    sex: "female",
    bmi: 27.9,
    children: 0,
    smoker: "no",
    region: "southwest",
  });

  const [loading, setLoading] = useState(false);
  const [prediction, setPrediction] = useState(null);
  const [error, setError] = useState("");

  const errors = useMemo(() => {
    const e = {};
    const age = Number(form.age);
    const bmi = Number(form.bmi);
    const children = Number(form.children);

    if (!Number.isFinite(age) || age < 18 || age > 64) e.age = "Age must be between 18 and 64.";
    if (!Number.isFinite(bmi) || bmi < 10 || bmi > 70) e.bmi = "BMI must be between 10 and 70.";
    if (!Number.isFinite(children) || children < 0 || children > 10) e.children = "Children must be between 0 and 10.";

    if (!sexes.includes(form.sex)) e.sex = "Select a valid sex.";
    if (!smokerOptions.includes(form.smoker)) e.smoker = "Select smoker yes/no.";
    if (!regions.includes(form.region)) e.region = "Select a valid region.";

    return e;
  }, [form]);

  const canSubmit = Object.keys(errors).length === 0 && !loading;

  const onChange = (key) => (evt) => {
    const value = evt.target.value;
    setForm((prev) => ({ ...prev, [key]: value }));
    setError("");
  };

  const onNumberChange = (key) => (evt) => {
    const value = evt.target.value;
    setForm((prev) => ({ ...prev, [key]: value }));
    setError("");
  };

  async function onSubmit(e) {
    e.preventDefault();
    setPrediction(null);
    setError("");

    if (!canSubmit) return;

    setLoading(true);
    try {
      const payload = {
        age: Number(form.age),
        sex: form.sex,
        bmi: Number(form.bmi),
        children: Number(form.children),
        smoker: form.smoker,
        region: form.region,
      };

      const res = await fetch(`${API_BASE}/predict`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload),
      });

      const data = await res.json();
      if (!res.ok) {
        throw new Error(data?.detail ?? "Request failed.");
      }

      setPrediction(data.predicted_charges);
    } catch (err) {
      setError(err?.message ?? "Something went wrong.");
    } finally {
      setLoading(false);
    }
  }

  return (
    <div  style={{ backgroundImage: "url(/bg1.avif)" }} className="min-h-screen bg-slate-950 text-slate-100 flex items-center">
      <div className="mx-auto max-w-4xl px-4 py-10">
        <header className="mb-8 text-center">
          <h1 className="text-5xl font-semibold tracking-tight text-black">Insurance Charges Estimator</h1>
          <p className="mt-2 text-slate-800">
            A simple ML-powered quote estimator using Multiple Linear Regression.
          </p>
        </header>

        <div className="grid gap-6 md:grid-cols-5">
          <section className="md:col-span-3 rounded-2xl border border-slate-800 bg-slate-900/70 p-6 shadow-lg">
            <h2 className="text-lg font-semibold">Your details</h2>
            <p className="mt-1 text-sm text-slate-300">
              Enter your info below and we’ll estimate annual charges.
            </p>

            <form className="mt-6 space-y-5" onSubmit={onSubmit}>
              <div className="grid gap-4 sm:grid-cols-2">
                <div>
                  <label className="text-sm text-slate-200">Age</label>
                  <input
                    type="number"
                    inputMode="numeric"
                    value={form.age}
                    onChange={onNumberChange("age")}
                    className={classNames(
                      "mt-1 w-full rounded-xl border bg-slate-950/40 px-3 py-2 outline-none",
                      errors.age ? "border-red-500" : "border-slate-800 focus:border-slate-500"
                    )}
                    placeholder="18 - 64"
                  />
                  {errors.age && <p className="mt-1 text-xs text-red-400">{errors.age}</p>}
                </div>

                <div>
                  <label className="text-sm text-slate-200">BMI</label>
                  <input
                    type="number"
                    step="0.1"
                    value={form.bmi}
                    onChange={onNumberChange("bmi")}
                    className={classNames(
                      "mt-1 w-full rounded-xl border bg-slate-950/40 px-3 py-2 outline-none",
                      errors.bmi ? "border-red-500" : "border-slate-800 focus:border-slate-500"
                    )}
                    placeholder="e.g. 27.9"
                  />
                  {errors.bmi && <p className="mt-1 text-xs text-red-400">{errors.bmi}</p>}
                </div>

                <div>
                  <label className="text-sm text-slate-200">Children</label>
                  <input
                    type="number"
                    inputMode="numeric"
                    value={form.children}
                    onChange={onNumberChange("children")}
                    className={classNames(
                      "mt-1 w-full rounded-xl border bg-slate-950/40 px-3 py-2 outline-none",
                      errors.children ? "border-red-500" : "border-slate-800 focus:border-slate-500"
                    )}
                    placeholder="0 - 10"
                  />
                  {errors.children && <p className="mt-1 text-xs text-red-400">{errors.children}</p>}
                </div>

                <div>
                  <label className="text-sm text-slate-200">Sex</label>
                  <select
                    value={form.sex}
                    onChange={onChange("sex")}
                    className={classNames(
                      "mt-1 w-full rounded-xl border bg-slate-950/40 px-3 py-2 outline-none",
                      errors.sex ? "border-red-500" : "border-slate-800 focus:border-slate-500"
                    )}
                  >
                    {sexes.map((s) => (
                      <option key={s} value={s}>
                        {s}
                      </option>
                    ))}
                  </select>
                  {errors.sex && <p className="mt-1 text-xs text-red-400">{errors.sex}</p>}
                </div>

                <div>
                  <label className="text-sm text-slate-200">Smoker</label>
                  <select
                    value={form.smoker}
                    onChange={onChange("smoker")}
                    className={classNames(
                      "mt-1 w-full rounded-xl border bg-slate-950/40 px-3 py-2 outline-none",
                      errors.smoker ? "border-red-500" : "border-slate-800 focus:border-slate-500"
                    )}
                  >
                    {smokerOptions.map((s) => (
                      <option key={s} value={s}>
                        {s}
                      </option>
                    ))}
                  </select>
                  {errors.smoker && <p className="mt-1 text-xs text-red-400">{errors.smoker}</p>}
                </div>

                <div>
                  <label className="text-sm text-slate-200">Region</label>
                  <select
                    value={form.region}
                    onChange={onChange("region")}
                    className={classNames(
                      "mt-1 w-full rounded-xl border bg-slate-950/40 px-3 py-2 outline-none",
                      errors.region ? "border-red-500" : "border-slate-800 focus:border-slate-500"
                    )}
                  >
                    {regions.map((r) => (
                      <option key={r} value={r}>
                        {r}
                      </option>
                    ))}
                  </select>
                  {errors.region && <p className="mt-1 text-xs text-red-400">{errors.region}</p>}
                </div>
              </div>

              {error && (
                <div className="rounded-xl border border-red-500/50 bg-red-500/10 p-3 text-sm text-red-200">
                  {error}
                </div>
              )}

              <button
                type="submit"
                disabled={!canSubmit}
                className={classNames(
                  "w-full rounded-xl px-4 py-2 font-medium transition",
                  canSubmit
                    ? "bg-slate-100 text-slate-900 hover:bg-white"
                    : "cursor-not-allowed bg-slate-800 text-slate-400"
                )}
              >
                {loading ? "Estimating..." : "Estimate charges"}
              </button>

              <p className="text-xs text-slate-400">
                Tip: Run the backend with <span className="font-mono">uvicorn api.main:app --reload</span>
              </p>
            </form>
          </section>

          <aside className="md:col-span-2 rounded-2xl border border-slate-800 bg-slate-900/60 p-6 shadow-lg">
            <h2 className="text-lg font-semibold">Result</h2>

            <div className="mt-6 rounded-2xl border border-slate-800 bg-slate-950/40 p-5">
              {prediction == null ? (
                <div>
                  <p className="text-sm text-slate-300">No estimate yet.</p>
                  <p className="mt-2 text-xs text-slate-400">
                    Fill the form and submit to see the prediction.
                  </p>
                </div>
              ) : (
                <div>
                  <p className="text-sm text-slate-300">Estimated annual charges</p>
                  <p className="mt-2 text-3xl font-semibold">{formatCurrency(prediction)}</p>
                  <p className="mt-2 text-xs text-slate-400">
                    This is a baseline linear regression estimate.
                  </p>
                </div>
              )}
            </div>

            <div className="mt-6 text-xs text-slate-400">
              <p className="font-medium text-slate-300">API:</p>
              <p className="mt-1 font-mono">{API_BASE}/predict</p>
            </div>
          </aside>
        </div>

        <footer className="mt-10 text-xs text-slate-500">
          Built with React + Tailwind + FastAPI.
        </footer>
      </div>
    </div>
  );
}
