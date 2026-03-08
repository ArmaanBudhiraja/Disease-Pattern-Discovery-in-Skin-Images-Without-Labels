import { useCallback, useState } from "react";
import { Upload, X, Image as ImageIcon } from "lucide-react";

interface ImageUploadProps {
  onImageSelect: (file: File) => void;
  preview: string | null;
  onClear: () => void;
}

const ImageUpload = ({ onImageSelect, preview, onClear }: ImageUploadProps) => {
  const [isDragging, setIsDragging] = useState(false);

  const handleDrop = useCallback(
    (e: React.DragEvent) => {
      e.preventDefault();
      setIsDragging(false);
      const file = e.dataTransfer.files[0];
      if (file && file.type.startsWith("image/")) onImageSelect(file);
    },
    [onImageSelect]
  );

  const handleFileInput = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (file) onImageSelect(file);
  };

  if (preview) {
    return (
      <div className="relative group">
        <div className="glass-card overflow-hidden">
          <img src={preview} alt="Uploaded skin image" className="w-full aspect-square object-cover rounded-lg" />
          <button
            onClick={onClear}
            className="absolute top-3 right-3 p-1.5 rounded-full bg-background/80 backdrop-blur-sm border border-border hover:bg-destructive/20 hover:border-destructive/50 transition-all"
          >
            <X className="w-4 h-4" />
          </button>
        </div>
      </div>
    );
  }

  return (
    <label
      onDragOver={(e) => { e.preventDefault(); setIsDragging(true); }}
      onDragLeave={() => setIsDragging(false)}
      onDrop={handleDrop}
      className={`glass-card flex flex-col items-center justify-center aspect-square cursor-pointer transition-all duration-300 ${
        isDragging ? "border-primary glow-teal scale-[1.02]" : "hover:border-primary/50 hover:bg-medical-surface-hover"
      }`}
    >
      <input type="file" accept="image/*" onChange={handleFileInput} className="hidden" />
      <div className="flex flex-col items-center gap-4 p-8">
        <div className="p-4 rounded-2xl bg-primary/10 border border-primary/20">
          <Upload className="w-8 h-8 text-primary" />
        </div>
        <div className="text-center">
          <p className="text-sm font-medium text-foreground">Drop skin image here</p>
          <p className="text-xs text-muted-foreground mt-1">or click to browse</p>
        </div>
        <div className="flex items-center gap-2 text-xs text-muted-foreground">
          <ImageIcon className="w-3 h-3" />
          <span>PNG, JPG up to 10MB</span>
        </div>
      </div>
    </label>
  );
};

export default ImageUpload;
