// GENERATED CODE BY json_serializer.dart - DO NOT MODIFY BY HAND
part of 'paraphrase.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

ParaphraseSerializer _$ParaphraseSerializerFromJson(Map<String, dynamic> json) {
  return ParaphraseSerializer()
    ..paraphrase = json['paraphrase'] as String
    ..exampleSentences = json['exampleSentences'] == null
        ? null
        : json['exampleSentences'].map<SentenceSerializer>((e) => SentenceSerializer.fromJson(e as Map<String, dynamic>)).toList();
}

Map<String, dynamic> _$ParaphraseSerializerToJson(ParaphraseSerializer instance) => <String, dynamic>{
    'paraphrase': instance.paraphrase,
    'exampleSentences': instance.exampleSentences
};
