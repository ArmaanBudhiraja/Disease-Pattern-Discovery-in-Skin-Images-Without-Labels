interface SimilarCasesProps {
  images: string[];
}

const SimilarCases = ({ images }: SimilarCasesProps) => {
  return (
    <div className="animate-fade-in" style={{ animationDelay: "0.3s" }}>
      <h3 className="text-sm font-semibold text-foreground mb-4 uppercase tracking-wider">Similar Cases from Dataset</h3>
      <div className="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-5 gap-3">
        {images.map((src, i) => (
          <div
            key={i}
            className="glass-card overflow-hidden group hover:border-primary/40 transition-all duration-300 hover:scale-[1.03]"
          >
            <div className="aspect-square bg-medical-surface relative overflow-hidden">
              <img src={src} alt={`Similar case ${i + 1}`} className="w-full h-full object-cover" />
              <div className="absolute inset-0 bg-gradient-to-t from-background/60 to-transparent opacity-0 group-hover:opacity-100 transition-opacity" />
              <div className="absolute bottom-2 left-2 opacity-0 group-hover:opacity-100 transition-opacity">
                <span className="text-xs font-mono text-foreground bg-background/60 backdrop-blur-sm px-2 py-0.5 rounded">
                  Case #{i + 1}
                </span>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default SimilarCases;
