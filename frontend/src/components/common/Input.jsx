export default function Input({
  label,
  placeholder = "",
  type = "text",
  value = "",
  onChange,
}) {
  return (
    <div className="flex flex-col gap-2">

      {label && (
        <label className="text-sm font-semibold text-slate-700">
          {label}
        </label>
      )}

      <input
        type={type}
        placeholder={placeholder}
        value={value}
        onChange={onChange}
        className="
          h-11
          w-full
          rounded-xl
          border
          border-slate-300
          bg-slate-50
          px-4
          text-sm
          text-slate-800
          placeholder:text-slate-400
          shadow-sm
          outline-none
          transition-all
          duration-200
          focus:bg-white
          focus:border-blue-600
          focus:ring-4
          focus:ring-blue-100
        "
      />

    </div>
  );
}