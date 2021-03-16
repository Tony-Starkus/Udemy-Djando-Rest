from rest_framework import serializers

from .models import Curso, Avaliacao


class AvaliacaoSerializer(serializers.ModelSerializer):

    class Meta:
        extra_kwargs = {
            'email': {'write_only': True}
        }
        model = Avaliacao
        fields = (
            'id',
            'curso',
            'nome',
            'email',
            'comentario',
            'avaliacao',
            'criacao',
            'ativo'
        )


class CursoSerializer(serializers.ModelSerializer):

    # Nested Relationship
    # avaliacoes = AvaliacaoSerializer(many=True, read_only=True)  # many: Um curso pode ter várias avaliações.

    # HyperLinked Related Field
    # Cria um array de strings com link/rota para acessar cada avaliação.
    # avaliacoes = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name="avaliacao-detail")

    # Primary Key Related Field
    avaliacoes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Curso
        fields = (
            'id',
            'titulo',
            'url',
            'criacao',
            'ativo',
            'avaliacoes'
        )
