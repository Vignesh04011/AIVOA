import Input from "../common/Input";
import Button from "../common/Button";

export default function MaterialsSection({
  formData,
  setFormData,
}) {
  return (
    <div className="space-y-5">

      <div>
        <h3 className="mb-3 text-sm font-semibold text-slate-700">
          Materials Shared / Samples Distributed
        </h3>

        <div className="flex gap-3">

          <Input
  placeholder="Search materials..."
  value={formData.materials_shared}
  onChange={(e) =>
    setFormData({
      ...formData,
      materials_shared: e.target.value,
    })
  }
/>

          <Button>
            Search / Add
          </Button>

        </div>

      </div>

    </div>
  );
}