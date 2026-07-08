import { useState } from "react";
import "./App.css";

function App() {
  const [formData, setFormData] = useState({
    hostname: "",
    ip_address: "",
    device_type: "router",
    vendor: "cisco",
    location: "london-dc1",
  });

  const [result, setResult] = useState(null);
  const [generatedConfig, setGeneratedConfig] = useState("");
  const [errorMessage, setErrorMessage] = useState("");
  const [loading, setLoading] = useState(false);

  function handleChange(event) {
    const { name, value } = event.target;

    setFormData({
      ...formData,
      [name]: value,
    });
  }

  async function handleGenerate(event) {
    event.preventDefault();

    const response = await fetch("http://127.0.0.1:8000/generate", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(formData),
    });

    const data = await response.json();

    setResult(data);

    if (data.status === "success") {
      setGeneratedConfig(data.config || data.generated_config || "");
    } else {
      setGeneratedConfig("");
    }
  }

  async function handleValidate(event) {
    event.preventDefault();

    setLoading(true);
    setErrorMessage("");
    setGeneratedConfig("");

    try {
      const response = await fetch("http://127.0.0.1:8000/validate", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(formData),
      });

      const data = await response.json();
      setResult(data);
    } catch (error) {
      setErrorMessage("Could not connect to backend");
    } finally {
      setLoading(false);
    }
  }


  return (
    <main className="app-container">
      <h1>Network Config Generator</h1>

      <form onSubmit={handleGenerate} className="config-form">
        <label>
          Hostname
          <input
            name="hostname"
            value={formData.hostname}
            onChange={handleChange}
            placeholder="london-dc1"
            required
          />
        </label>

        <label>
          IP Address
          <input
            name="ip_address"
            value={formData.ip_address}
            onChange={handleChange}
            placeholder="192.168.1.1"
            required
          />
        </label>

        <label>
          Device Type
          <select
            name="device_type"
            value={formData.device_type}
            onChange={handleChange}
            required
          >
            <option value="router">Router</option>
            <option value="switch">Switch</option>
          </select>
        </label>

        <label>
          Vendor
          <select name="vendor" value={formData.vendor} onChange={handleChange} required>
            <option value="cisco">Cisco</option>
            <option value="juniper">Juniper</option>
            
          </select>
        </label>

        <label>
          Location
          <select
            name="location"
            value={formData.location}
            onChange={handleChange}
            required
          >
            <option value="london-dc1">London DC1</option>
            <option value="manchester-office">Manchester Office</option>
            <option value="glasgow-dc1">Glasgow DC1</option>
          </select>
        </label>

        <button type="submit">Generate Config</button>
        <button type ="button" onClick={handleValidate}>Validate Config</button>
      </form>

      {result && result.status === "error" && (
        <section className="error-box">
          <h2>Validation Errors</h2>
          <ul>
            {result.errors.map((error, index) => (
              <li key={index}>{error}</li>
            ))}
          </ul>
        </section>
      )}

      {generatedConfig && (
        <section className="output-section">
          <h2>Generated Config</h2>
          <pre>{generatedConfig}</pre>
        </section>
      )}
    </main>
  );
}

export default App;