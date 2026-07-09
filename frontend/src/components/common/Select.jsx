export default function Select({
  label,
  options = [],
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

      <select
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
          shadow-sm
          outline-none
          transition-all
          duration-200
          focus:bg-white
          focus:border-blue-600
          focus:ring-4
          focus:ring-blue-100
        "
      >
        <option value="">Select an option</option>

        {options.map((option) => (
          <option
            key={option}
            value={option}
          >
            {option}
          </option>
        ))}

      </select>

    </div>
  );
}