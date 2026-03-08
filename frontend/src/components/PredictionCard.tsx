import { Shield, AlertTriangle } from "lucide-react";

interface PredictionCardProps {
  disease: string;
  confidence: number;
  description: string;
}

const PredictionCard = ({ disease, confidence, description }: PredictionCardProps) => {
  const isHighRisk = ["Melanoma", "Squamous cell carcinoma"].includes(disease);

  return (
    <div className={`glass-card p-6 glow-teal animate-fade-in ${isHighRisk ? "border-medical-danger/40" : ""}`}>
      <div className="flex items-start justify-between mb-4">
        <div className="flex items-center gap-3">
          <div className={`p-2.5 rounded-xl ${isHighRisk ? "bg-destructive/15 border border-destructive/30" : "bg-primary/15 border border-primary/30"}`}>
            {isHighRisk ? <AlertTriangle className="w-5 h-5 text-destructive" /> : <Shield className="w-5 h-5 text-primary" />}
          </div>
          <div>
            <p className="text-xs font-medium text-muted-foreground uppercase tracking-wider">Predicted Diagnosis</p>
            <h2 className="text-xl font-bold text-foreground mt-0.5">{disease}</h2>
          </div>
        </div>
        <div className="text-right">
          <p className="text-xs text-muted-foreground">Confidence</p>
          <p className="text-2xl font-bold text-gradient">{(confidence * 100).toFixed(1)}%</p>
        </div>
      </div>
      <p className="text-sm text-muted-foreground leading-relaxed">{description}</p>
    </div>
  );
};

export default PredictionCard;
