import { Scan } from "lucide-react";

const LoadingOverlay = () => {
  return (
    <div className="glass-card p-12 flex flex-col items-center justify-center gap-6 animate-fade-in">
      <div className="relative">
        <div className="w-20 h-20 rounded-full border-2 border-primary/30 animate-spin" style={{ borderTopColor: "hsl(var(--primary))" }} />
        <Scan className="w-8 h-8 text-primary absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 animate-pulse" />
      </div>
      <div className="text-center">
        <p className="text-sm font-medium text-foreground">Analyzing Image</p>
        <p className="text-xs text-muted-foreground mt-1">Running AI classification model...</p>
      </div>
      <div className="flex gap-1.5">
        {[0, 1, 2, 3, 4].map((i) => (
          <div
            key={i}
            className="w-2 h-2 rounded-full bg-primary animate-pulse"
            style={{ animationDelay: `${i * 0.15}s` }}
          />
        ))}
      </div>
    </div>
  );
};

export default LoadingOverlay;
