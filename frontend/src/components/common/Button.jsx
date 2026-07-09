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
        inline-flex
        items-center
        justify-center
        rounded-lg
        px-4
        py-2.5
        text-sm
        font-semibold
        transition-all
        duration-200
        shadow-sm
        disabled:opacity-50
        disabled:cursor-not-allowed
        ${className}
      `}
    >
      {children}
    </button>
  );
}