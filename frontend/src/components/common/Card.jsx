export default function Card({ children, className = "" }) {
  return (
    <div
      className={`
        rounded-2xl
        border
        border-slate-200
        bg-white
        shadow-md
        hover:shadow-lg
        transition-all
        duration-200
        p-6
        ${className}
      `}
    >
      {children}
    </div>
  );
}