import Input from "../common/Input";
import Button from "../common/Button";

export default function MaterialsSection() {
  return (
    <div className="space-y-5">

      <div>
        <h3 className="mb-3 text-sm font-semibold text-slate-700">
          Materials Shared / Samples Distributed
        </h3>

        <div className="flex gap-3">

          <Input
            placeholder="Search materials..."
          />

          <Button>
            Search / Add
          </Button>

        </div>

      </div>

    </div>
  );
}