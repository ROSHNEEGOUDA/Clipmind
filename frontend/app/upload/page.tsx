"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";

export default function Upload() {
  const [file, setFile] = useState<File | null>(null);
  const [loading, setLoading] = useState(false);
  const [message, setMessage] = useState("");
  const router = useRouter();

  const handleUpload = async () => {
    if (!file) {
      setMessage("Please select a video file");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {
      setLoading(true);
      setMessage("Uploading and processing...");

      const res = await fetch("http://127.0.0.1:8000/upload/", {
        method: "POST",
        body: formData,
      });

      if (!res.ok) throw new Error("Upload failed");

      const data = await res.json();
      router.push(`/results?jobId=${data.job_id}`);
    } catch {
      setMessage("Upload failed. Please check backend connection.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <main className="relative min-h-screen bg-black text-white flex items-center justify-center px-4 overflow-hidden">
      
      {/* Background Glow */}
      <div className="absolute inset-0">
        <div className="absolute top-1/3 left-1/2 -translate-x-1/2 w-[500px] h-[500px] bg-purple-600/30 rounded-full blur-[140px]" />
      </div>

      {/* Card */}
      <div className="relative z-10 w-full max-w-xl bg-gray-900/80 backdrop-blur-xl border border-gray-800 rounded-2xl p-8 shadow-xl">
        
        <h2 className="text-3xl font-bold mb-2 text-center">
          Upload Your Video
        </h2>
        <p className="text-gray-400 text-center mb-8">
          Turn long videos into viral-ready clips using AI
        </p>

        {/* Upload Box */}
        <label className="flex flex-col items-center justify-center border-2 border-dashed border-gray-700 rounded-xl p-6 cursor-pointer hover:border-purple-500 transition mb-4">
          <input
            type="file"
            accept="video/*"
            className="hidden"
            onChange={(e) => setFile(e.target.files?.[0] || null)}
          />

          <div className="text-center">
            <p className="text-lg font-medium">
              {file ? file.name : "Click to upload a video"}
            </p>
            <p className="text-sm text-gray-500 mt-1">
              MP4, MOV, AVI supported
            </p>
          </div>
        </label>

        {/* YouTube Placeholder */}
        <input
          type="text"
          placeholder="YouTube URL (coming soon)"
          disabled
          className="w-full p-3 bg-gray-800 rounded-xl opacity-50 mb-6"
        />

        {/* Button */}
        <button
          onClick={handleUpload}
          disabled={loading}
          className={`w-full py-4 rounded-xl text-lg font-semibold transition
            ${loading
              ? "bg-gray-700 cursor-not-allowed"
              : "bg-gradient-to-r from-purple-600 to-pink-600 hover:scale-[1.02] hover:shadow-lg hover:shadow-purple-600/30"
            }`}
        >
          {loading ? "Processing..." : "Process Video"}
        </button>

        {/* Status Message */}
        {message && (
          <p className="mt-4 text-center text-sm text-gray-300">
            {message}
          </p>
        )}
      </div>
    </main>
  );
}
