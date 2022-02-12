import graphene
from user.schema import (
    AuthMutation,
    AuthQuery,
    HospitalQuery,
    PatientQuery,
    PatientMutation,
    PatientAuthorizedHospitalQuery,
    PatientAuthorizedHospitalMutation,
)
from patientrecord.schema import (
    MedicineRecordQuery,
    DoctorNotesQuery,
    TestResultQuery,
    MedicinePrescriptionMutation,
    MedicineRecordMutation,
    DoctorNotesMutation,
    TestResultMutation,
)

from resources.schema import HospitalResourceQuery
from resources.schema import HospitalResourceMutation

from opd.schema import DoctorQuery, DoctorPatientAssignedQuery
from opd.schema import DoctorMutation, DoctorPatientAssignedMutation


class Query(
    DoctorQuery,
    DoctorPatientAssignedQuery,
    HospitalResourceQuery,
    PatientQuery,
    PatientAuthorizedHospitalQuery,
    HospitalQuery,
    MedicineRecordQuery,
    DoctorNotesQuery,
    TestResultQuery,
    AuthQuery,
    graphene.ObjectType,
):
    pass


class Mutation(
    DoctorMutation,
    DoctorPatientAssignedMutation,
    HospitalResourceMutation,
    PatientMutation,
    PatientAuthorizedHospitalMutation,
    MedicinePrescriptionMutation,
    MedicineRecordMutation,
    DoctorNotesMutation,
    TestResultMutation,
    AuthMutation,
    graphene.ObjectType,
):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
