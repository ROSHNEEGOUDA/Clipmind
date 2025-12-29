"use client";

import { useEffect, useState } from "react";
import api from "../../lib/apiInstance";

/* ------------------ TYPES ------------------ */

interface Clip {
  video: string;
  caption?: string;
  hashtags?: string[];
  ocr_text?: string[];
}

interface ResultsResponse {
  status: "processing" | "done" | "failed";
  clips: Clip[];
}

/* ------------------ PAGE ------------------ */

export default function Results({ searchParams }: any) {
  const jobId = searchParams.jobId;

  const [clips, setClips] = useState<Clip[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    if (!jobId) return;

    let interval: NodeJS.Timeout;

    const fetchResults = async () => {
      try {
        const data = await api.get<ResultsResponse>(`/results/${jobId}`);

        if (data.clips && data.clips.length > 0) {
          setClips(data.clips);
          setLoading(false);
          clearInterval(interval);
        }

        if (data.status === "failed") {
          setError("Video processing failed.");
          setLoading(false);
          clearInterval(interval);
        }
      } catch (err) {
        console.error("Polling error", err);
      }
    };

    fetchResults();
    interval = setInterval(fetchResults, 3000);

    return () => clearInterval(interval);
  }, [jobId]);

  return (
    <main className="relative min-h-screen bg-black text-white px-6 py-10 overflow-hidden">
      {/* Background Glow */}
      <div className="absolute inset-0">
        <div
          className="absolute top-1/4 left-1/2 -translate-x-1/2
                        w-[600px] h-[600px] bg-purple-600/25
                        rounded-full blur-[160px]"
        />
      </div>

      {/* Header */}
      <div className="relative z-10 max-w-7xl mx-auto mb-10">
        <h1 className="text-4xl font-extrabold mb-2">Your AI-Generated Reel</h1>
        <p className="text-gray-400">
          We’re crafting highlights from your video
        </p>
      </div>

      {/* Content */}
      <div className="relative z-10 max-w-7xl mx-auto">
        {/* LOADING */}
        {loading && (
          <div className="flex flex-col items-center justify-center py-20">
            <div
              className="w-16 h-16 border-4 border-purple-500
                            border-t-transparent rounded-full animate-spin mb-6"
            />
            <p className="text-gray-400 text-lg">
              Analyzing & generating your reel…
            </p>
            <p className="text-gray-600 text-sm mt-2">
              This usually takes under a minute
            </p>
          </div>
        )}

        {/* ERROR */}
        {!loading && error && (
          <p className="text-red-500 text-center">{error}</p>
        )}

        {/* RESULTS */}
        {!loading && clips.length > 0 && (
          <div className="grid gap-8 sm:grid-cols-2 lg:grid-cols-3">
            {clips.map((clip, i) => (
              <div
                key={i}
                className="bg-gray-900/80 backdrop-blur
                           border border-gray-800 rounded-2xl
                           p-4 shadow-lg
                           hover:shadow-purple-600/20 transition"
              >
                <video
                  controls
                  className="rounded-xl w-full aspect-[9/16] bg-black"
                  src={`http://127.0.0.1:8000${clip.video}`}
                />

                {/* CAPTION */}
                {clip.caption && (
                  <p className="mt-3 text-sm text-gray-300 whitespace-pre-line">
                    {clip.caption}
                  </p>
                )}

                {/* HASHTAGS */}
                {clip.hashtags && clip.hashtags.length > 0 && (
                  <p className="mt-2 text-sm text-purple-400">
                    {clip.hashtags.join(" ")}
                  </p>
                )}

                {/* DOWNLOAD */}
                <a
                  href={`http://127.0.0.1:8000${clip.video}`}
                  download
                  className="mt-4 block text-center py-3 rounded-xl font-semibold
                             bg-gradient-to-r from-purple-600 to-pink-600
                             hover:scale-[1.02]
                             hover:shadow-lg hover:shadow-purple-600/30
                             transition"
                >
                  Download HD
                </a>
              </div>
            ))}
          </div>
        )}
      </div>
    </main>
  );
}
