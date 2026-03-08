import { Activity, Brain } from "lucide-react";

const Header = () => {
  return (
    <header className="border-b border-border/50 bg-card/50 backdrop-blur-xl sticky top-0 z-50">
      <div className="container mx-auto px-4 h-16 flex items-center justify-between">
        <div className="flex items-center gap-3">
          <div className="p-2 rounded-xl gradient-teal">
            <Brain className="w-5 h-5 text-primary-foreground" />
          </div>
          <div>
            <h1 className="text-base font-bold text-foreground tracking-tight">Skin Disease Detection System</h1>
            <p className="text-[10px] text-muted-foreground uppercase tracking-widest">Dermatology Analysis</p>
          </div>
        </div>
        <div className="flex items-center gap-2 text-xs text-muted-foreground">
          <Activity className="w-3.5 h-3.5 text-medical-green" />
          <span className="hidden sm:inline">System Online</span>
        </div>
      </div>
    </header>
  );
};

export default Header;
