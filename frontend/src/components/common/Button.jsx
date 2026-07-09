export default function Button({
  children,
  className = "",
  type = "button",
  onClick,
  disabled = false,
}) {
  return (
    <button
      type={type}
      onClick={onClick}
      disabled={disabled}
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