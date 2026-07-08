export default function MainLayout({ left, right }) {
  return (
    <div className="grid grid-cols-12 gap-6">
      <div className="col-span-7">{left}</div>

      <div className="col-span-5">{right}</div>
    </div>
  );
}