export default function Home() {
  return (
    <main className="relative min-h-screen bg-black text-white flex items-center justify-center overflow-hidden">
      
      {/* Background glow */}
      <div className="absolute inset-0">
        <div className="absolute top-1/3 left-1/2 -translate-x-1/2 w-[600px] h-[600px] bg-purple-600/30 rounded-full blur-[140px]" />
        <div className="absolute bottom-0 right-1/4 w-[400px] h-[400px] bg-pink-500/20 rounded-full blur-[120px]" />
      </div>

      {/* Content */}
      <div className="relative z-10 max-w-3xl text-center px-6">
        
        <h1 className="text-5xl md:text-6xl font-extrabold leading-tight mb-6">
          Turn{" "}
          <span className="bg-gradient-to-r from-purple-400 to-pink-500 bg-clip-text text-transparent">
            Hours
          </span>{" "}
          Into{" "}
          <span className="bg-gradient-to-r from-purple-400 to-pink-500 bg-clip-text text-transparent">
            Highlights
          </span>{" "}
          — Instantly
        </h1>

        <p className="text-gray-400 text-lg md:text-xl mb-10">
          Free AI-powered tool that transforms long videos into
          viral-ready reels, shorts, and clips in minutes.
        </p>

        <div className="flex flex-col sm:flex-row gap-4 justify-center items-center">
          <a
            href="/upload"
            className="px-8 py-4 rounded-2xl text-lg font-semibold 
                       bg-gradient-to-r from-purple-600 to-pink-600 
                       hover:scale-105 hover:shadow-xl hover:shadow-purple-600/30
                       transition-all duration-300"
          >
            Start Creating Free
          </a>

          <span className="text-gray-500 text-sm">
            No watermark • No credit card
          </span>
        </div>

        {/* Social proof */}
        <p className="mt-10 text-gray-500 text-sm">
          Trusted by creators, podcasters, and agencies worldwide
        </p>
      </div>
    </main>
  );
}
