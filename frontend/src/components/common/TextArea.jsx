export default function TextArea({
  label,
  placeholder = "",
  rows = 4,
  value = "",
  onChange,
}) {
  return (
    <div className="flex flex-col gap-2">

      {label && (
        <label className="text-sm font-medium text-slate-700">
          {label}
        </label>
      )}

      <textarea
        rows={rows}
        placeholder={placeholder}
        value={value}
        onChange={onChange}
        className="
          w-full
          rounded-md
          border
          border-slate-300
          bg-white
          p-3
          text-sm
          outline-none
          resize-none
          transition
          focus:border-blue-500
          focus:ring-2
          focus:ring-blue-200
        "
      />

    </div>
  );
}