export default function Button({
  children,
  className = "",
  type = "button",
}) {
  return (
    <button
      type={type}
      className={`
        rounded-md
        border
        border-slate-300
        bg-white
        px-4
        py-2
        text-sm
        font-medium
        hover:bg-slate-100
        transition
        ${className}
      `}
    >
      {children}
    </button>
  );
}