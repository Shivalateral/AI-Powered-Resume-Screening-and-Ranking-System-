import React, { useState } from "react";

function App() {
  const [jobDesc, setJobDesc] = useState("");
  const [resumes, setResumes] = useState([]);
  const [rankedResumes, setRankedResumes] = useState([]);

  const handleFileChange = (e) => {
    setResumes(e.target.files);
  };

  const handleSubmit = async () => {
    const formData = new FormData();
    formData.append("job_desc", jobDesc);
    for (let i = 0; i < resumes.length; i++) {
      formData.append("resumes", resumes[i]);
    }

    const response = await fetch("http://localhost:5000/upload", {
      method: "POST",
      body: formData,
    });

    const data = await response.json();
    setRankedResumes(data);
  };

  return (
    <div>
      <h1>AI Resume Screening</h1>
      <textarea
        placeholder="Enter Job Description"
        onChange={(e) => setJobDesc(e.target.value)}
      />
      <input type="file" multiple accept="application/pdf" onChange={handleFileChange} />
      <button onClick={handleSubmit}>Upload & Rank</button>
      <ul>
        {rankedResumes.map((item, index) => (
          <li key={index}>{item.resume} - Score: {item.score}</li>
        ))}
      </ul>
    </div>
  );
}

export default App;
