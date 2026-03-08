import { useState, useCallback } from "react";
import { Scan } from "lucide-react";
import { toast } from "sonner";
import Header from "@/components/Header";
import ImageUpload from "@/components/ImageUpload";
import PredictionCard from "@/components/PredictionCard";
import ProbabilityChart from "@/components/ProbabilityChart";
import ProcessingGrid from "@/components/ProcessingGrid";
import SimilarCases from "@/components/SimilarCases";
import LoadingOverlay from "@/components/LoadingOverlay";

const DISEASE_DESCRIPTIONS: Record<string, string> = {
  "Actinic keratosis": "A rough, scaly patch on the skin caused by years of sun exposure. Often found on face, lips, ears, forearms, scalp, and neck.",
  "Atopic Dermatitis": "A chronic condition that makes skin red and itchy. It is common in children but can occur at any age.",
  "Benign keratosis": "A non-cancerous skin growth that originates in keratinocytes. These lesions are very common in older adults.",
  "Dermatofibroma": "A common benign fibrous nodule usually found on the skin of the lower legs.",
  "Melanoma": "The most serious type of skin cancer, developing in melanocytes. Early detection is critical for treatment.",
  "Melanocytic nevus": "A common type of melanocytic tumor, more commonly called a mole. Generally benign.",
  "Squamous cell carcinoma": "The second most common form of skin cancer, arising from squamous cells in the epidermis.",
  "Tinea Ringworm Candidiasis": "Fungal infections of the skin caused by dermatophytes or candida species.",
  "Vascular lesion": "Abnormalities of blood vessels in the skin, including angiomas, pyogenic granulomas, and hemorrhage.",
};

const DISEASES = Object.keys(DISEASE_DESCRIPTIONS);

const API_URL = "http://localhost:8000/predict";

const Index = () => {
  const [preview, setPreview] = useState<string | null>(null);
  const [file, setFile] = useState<File | null>(null);
  const [loading, setLoading] = useState(false);
  const [results, setResults] = useState<{
    predicted: string;
    confidence: number;
    probabilities: { disease: string; probability: number }[];
    processingImages: { label: string; src: string }[];
    similarImages: string[];
  } | null>(null);

  const handleImageSelect = useCallback((f: File) => {
    setFile(f);
    setPreview(URL.createObjectURL(f));
    setResults(null);
  }, []);

  const handleClear = useCallback(() => {
    setFile(null);
    setPreview(null);
    setResults(null);
  }, []);

  const handleAnalyze = useCallback(async () => {
    if (!file) return;
    setLoading(true);

    try {
      const formData = new FormData();
      formData.append("file", file);
      const res = await fetch(API_URL, { method: "POST", body: formData });
      if (!res.ok) throw new Error("API request failed");
      const data = await res.json();

      const probabilities = Object.entries(data.probabilities).map(
        ([disease, probability]) => ({ disease, probability: probability as number })
      );
      probabilities.sort((a, b) => b.probability - a.probability);

      const pi = data.processing_images;
      const toDataUrl = (b64: string) => b64.startsWith("data:") ? b64 : `data:image/png;base64,${b64}`;

      setResults({
        predicted: data.prediction,
        confidence: probabilities[0].probability,
        probabilities,
        processingImages: [
          { label: "Original Image", src: toDataUrl(pi.original) },
          { label: "Blurred Image", src: toDataUrl(pi.blur) },
          { label: "Grayscale Image", src: toDataUrl(pi.grayscale) },
          { label: "Segmented Lesion", src: toDataUrl(pi.lesion) },
          { label: "Lesion Boundary", src: toDataUrl(pi.boundary) },
          { label: "Heatmap Overlay", src: toDataUrl(pi.heatmap) },
        ],
        similarImages: data.similar_images.map((b64: string) =>
          b64.startsWith("data:") ? b64 : `data:image/png;base64,${b64}`
        ),
      });
    } catch (err) {
      console.error("Analysis failed:", err);
      toast.error("Failed to connect to the backend. Make sure your Python server is running.");
    } finally {
      setLoading(false);
    }
  }, [file]);

  return (
    <div className="min-h-screen bg-background">
      <Header />

      <main className="container mx-auto px-4 py-8">
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-6">
          {/* Left Panel */}
          <div className="lg:col-span-4 xl:col-span-3 space-y-4">
            <div className="glass-card p-4">
              <h2 className="text-xs font-semibold text-muted-foreground uppercase tracking-widest mb-4">Input Image</h2>
              <ImageUpload onImageSelect={handleImageSelect} preview={preview} onClear={handleClear} />
              <button
                onClick={handleAnalyze}
                disabled={!file || loading}
                className="w-full mt-4 py-3 px-4 rounded-xl font-medium text-sm transition-all duration-300 flex items-center justify-center gap-2 disabled:opacity-40 disabled:cursor-not-allowed gradient-teal text-primary-foreground hover:opacity-90 active:scale-[0.98]"
              >
                <Scan className="w-4 h-4" />
                {loading ? "Analyzing..." : "Analyze Image"}
              </button>
            </div>
          </div>

          {/* Right Panel */}
          <div className="lg:col-span-8 xl:col-span-9 space-y-6">
            {loading && <LoadingOverlay />}

            {!loading && !results && (
              <div className="glass-card p-16 flex flex-col items-center justify-center text-center">
                <div className="p-5 rounded-2xl bg-secondary mb-5">
                  <Scan className="w-10 h-10 text-muted-foreground" />
                </div>
                <h3 className="text-lg font-semibold text-foreground mb-2">No Analysis Yet</h3>
                <p className="text-sm text-muted-foreground max-w-md">
                  Upload a skin lesion image and click "Analyze Image" to get an AI-powered diagnosis with detailed processing visualization.
                </p>
              </div>
            )}

            {!loading && results && (
              <div className="space-y-6">
                <div className="grid grid-cols-1 xl:grid-cols-2 gap-6">
                  <PredictionCard
                    disease={results.predicted}
                    confidence={results.confidence}
                    description={DISEASE_DESCRIPTIONS[results.predicted] || ""}
                  />
                  <ProbabilityChart probabilities={results.probabilities} />
                </div>
                <ProcessingGrid images={results.processingImages} />
                <SimilarCases images={results.similarImages} />
              </div>
            )}
          </div>
        </div>
      </main>
    </div>
  );
};

export default Index;
