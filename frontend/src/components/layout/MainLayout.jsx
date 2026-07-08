export default function MainLayout({ left, right }) {
  return (
    <div className="grid grid-cols-12 gap-6">
      <div className="col-span-8">{left}</div>

      <div className="col-span-4">{right}</div>
    </div>
  );
}