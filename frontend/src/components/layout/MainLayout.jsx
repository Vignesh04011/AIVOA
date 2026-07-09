export default function MainLayout({ left, right }) {
  return (
    <div className="grid grid-cols-12 gap-8 items-start">

      {/* Interaction Form */}
      <div className="col-span-12 lg:col-span-8">
        {left}
      </div>

      {/* AI Assistant */}
      <div className="col-span-12 lg:col-span-4">
        <div className="sticky top-6">
          {right}
        </div>
      </div>

    </div>
  );
}