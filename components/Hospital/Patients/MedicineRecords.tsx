import { useAuth } from '../../../lib/auth'

import { useCreateMedicineRecordMutation } from '../../../graphql/generated'

const MedicineRecords = ({ pid, data }) => {
    const { user } = useAuth()
    const [createMedicineRecord] = useCreateMedicineRecordMutation()

    const handleSubmit = (e) => {
        e.preventDefault();
        const formData = new FormData(e.currentTarget)

        createMedicineRecord({
            variables: {
                patientId: pid,
                prescriptions: formData.get('prescriptions'),
            }
        })
    }
    return (
        <div>
            <h2>Medicine Records</h2>
            {data?.patient?.medicinerecordSet.length > 0 &&
                <>
                    {data.patient.medicinerecordSet.map(record => {
                        return (
                            <div key={record.id}>
                                {record.prescription}
                            </div>
                        )
                    })}
                </>
            }
            {user?.isDoctor && (<form
                className="flex gap-4"
                onSubmit={handleSubmit}
            >
                <input
                    type="text"
                    id="prescriptions"
                    name="prescriptions"
                    className="rounded-lg border border-transparent py-2 px-4 text-gray-700 placeholder-gray-400 shadow-sm focus:border-transparent focus:outline-none focus:ring-2 focus:ring-sky-600"
                    placeholder="Prescription Name"
                    required
                />
                <button
                    type="submit"
                    className="rounded-lg bg-sky-600 py-2 px-4 text-center font-semibold text-white shadow-md transition duration-200 ease-in hover:bg-sky-700 focus:outline-none focus:ring-2 focus:ring-sky-500 focus:ring-offset-2 focus:ring-offset-sky-200"
                >
                    Create prescription
                </button>
            </form>)}
        </div>
    )
}

export default MedicineRecords
