interface ProcessingGridProps {
  images: { label: string; src: string }[];
}

const ProcessingGrid = ({ images }: ProcessingGridProps) => {
  return (
    <div className="animate-fade-in" style={{ animationDelay: "0.2s" }}>
      <h3 className="text-sm font-semibold text-foreground mb-4 uppercase tracking-wider">Processing Pipeline</h3>
      <div className="grid grid-cols-2 lg:grid-cols-3 gap-3">
        {images.map((img, i) => (
          <div
            key={img.label}
            className="glass-card overflow-hidden group hover:border-primary/40 transition-all duration-300 hover:scale-[1.02]"
            style={{ animationDelay: `${i * 0.08}s` }}
          >
            <div className="aspect-square bg-medical-surface relative overflow-hidden">
              <img src={img.src} alt={img.label} className="w-full h-full object-cover" />
              <div className="absolute inset-0 bg-gradient-to-t from-background/80 to-transparent opacity-0 group-hover:opacity-100 transition-opacity" />
            </div>
            <div className="p-3">
              <p className="text-xs font-medium text-muted-foreground group-hover:text-foreground transition-colors text-center">
                {img.label}
              </p>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default ProcessingGrid;
