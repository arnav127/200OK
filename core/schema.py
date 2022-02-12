import graphene
from user.schema import UserQuery, UserMutation
from patientrecord.schema import PatientRecordQuery, PatientRecordMutation

from resources.schema import HospitalResourceQuery
from resources.schema import HospitalResourceMutation

from opd.schema import OpdQuery, OpdMutation


class Query(
    OpdQuery,
    HospitalResourceQuery,
    UserQuery,
    graphene.ObjectType,
):
    pass


class Mutation(
    OpdMutation,
    HospitalResourceMutation,
    UserMutation,
    graphene.ObjectType,
):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
