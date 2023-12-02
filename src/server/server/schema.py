import graphene
from graphene_django import DjangoObjectType
from .models import Region, Diagnostic

class DiagnosticType(DjangoObjectType):
    class Meta: 
        model = Diagnostic
        
class RegionType(DjangoObjectType):
    class Meta:
        model = Region
        
class Query(graphene.ObjectType):
    allRegions = graphene.List(RegionType, description="List of all regions")
    allDiagnostics = graphene.List(DiagnosticType, description="List of all diagnostics")
    
    def resolve_all_regions(self, info):
        return Region.objects.all()
    
    def resolve_all_diagnostics(self, info):
        return Diagnostic.objects.all()
    
schema = graphene.Schema(query=Query)