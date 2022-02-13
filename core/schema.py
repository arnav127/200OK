import graphene
from user.schema import UserQuery, UserMutation
from patientrecord.schema import PatientRecordQuery, PatientRecordMutation

from resources.schema import HospitalResourceQuery
from resources.schema import HospitalResourceMutation

from opd.schema import OpdQuery, OpdMutation

from mayodata.schema import DiseaseInfoQuery


class Query(
    DiseaseInfoQuery,
    OpdQuery,
    HospitalResourceQuery,
    PatientRecordQuery,
    UserQuery,
    graphene.ObjectType,
):
    """All graphql queries"""
    pass


class Mutation(
    OpdMutation,
    HospitalResourceMutation,
    PatientRecordMutation,
    UserMutation,
    graphene.ObjectType,
):
    """All graphql mutations"""
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
