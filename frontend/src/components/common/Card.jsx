export default function Card({ children, className = "" }) {
  return (
    <div
      className={`
        rounded-xl
        border
        border-slate-200
        bg-white
        shadow-sm
        p-6
        ${className}
      `}
    >
      {children}
    </div>
  );
}