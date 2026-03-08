interface ProbabilityChartProps {
  probabilities: { disease: string; probability: number }[];
}

const ProbabilityChart = ({ probabilities }: ProbabilityChartProps) => {
  const sorted = [...probabilities].sort((a, b) => b.probability - a.probability);
  const max = sorted[0]?.probability || 1;

  return (
    <div className="glass-card p-6 animate-fade-in" style={{ animationDelay: "0.1s" }}>
      <h3 className="text-sm font-semibold text-foreground mb-4 uppercase tracking-wider">Classification Probabilities</h3>
      <div className="space-y-3">
        {sorted.map((item, i) => (
          <div key={item.disease} className="group" style={{ animationDelay: `${i * 0.05}s` }}>
            <div className="flex justify-between items-center mb-1">
              <span className="text-xs text-muted-foreground group-hover:text-foreground transition-colors truncate mr-2">
                {item.disease}
              </span>
              <span className="text-xs font-mono text-primary">{(item.probability * 100).toFixed(1)}%</span>
            </div>
            <div className="h-2 bg-secondary rounded-full overflow-hidden">
              <div
                className="h-full rounded-full transition-all duration-700 ease-out gradient-teal"
                style={{
                  width: `${(item.probability / max) * 100}%`,
                  opacity: 0.4 + (item.probability / max) * 0.6,
                }}
              />
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default ProbabilityChart;
