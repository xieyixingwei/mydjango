import 'package:flutter/material.dart';
import 'package:flutter_prj/common/global.dart';
import 'package:flutter_prj/routes/tabs/practice/sentence_pattern_practice.dart';
import 'package:flutter_prj/routes/tabs/practice/sentence_practice.dart';
import 'package:flutter_prj/routes/tabs/practice/word_practice.dart';
import 'package:flutter_prj/serializers/index.dart';


class TabPractice extends StatefulWidget {
  TabPractice({Key key}) : super(key: key);

  @override
  _TabPractice createState() => _TabPractice();
}


class _TabPractice extends State<TabPractice> {

  @override
  Widget build(BuildContext context) =>
    Scaffold(
      appBar: AppBar(
        title: Text('练习'),
        centerTitle: true,
      ),
      body: SingleChildScrollView(
        padding: EdgeInsets.fromLTRB(6, 6, 6, 6),
        child: Center(
          child: Wrap(
            spacing: 10,
            runSpacing: 10,
            alignment: WrapAlignment.spaceAround,
            runAlignment: WrapAlignment.spaceAround,
            children: [
              _card(context, '单词', () async {
                if(Global.localStore.user.studyPlan.wordCategories.isEmpty) return;
                var studyWord = StudyWordSerializer();
                studyWord.filter..foreignUser = Global.localStore.user.id
                                          ..familiarity__lte = 4
                                          ..inplan = true;
                var studyWords = await studyWord.list();
                Navigator.of(context).push(
                  MaterialPageRoute(
                    builder: (context) => WordPracticePage(studyWords: studyWords),
                  )
                );
              }),
              _card(context, '句子', () async {
                if(Global.localStore.user.studyPlan.sentenceCategories.isEmpty) return;
                var studySentence = StudySentenceSerializer();
                studySentence.filter..foreignUser = Global.localStore.user.id
                                          ..familiarity__lte = 4
                                          ..inplan = true;
                var studySentences = await studySentence.list();
                Navigator.of(context).push(
                  MaterialPageRoute(
                    builder: (context) => SentencePracticePage(studySentences: studySentences),
                  )
                );
              }),
              _card(context, '固定表达', () async {
                if(Global.localStore.user.studyPlan.sentencePatternCategories.isEmpty) return;
                var studySentencePattern = StudySentencePatternSerializer();
                studySentencePattern.filter..foreignUser = Global.localStore.user.id
                                          ..familiarity__lte = 4
                                          ..inplan = true;
                var studySentencePatterns = await studySentencePattern.list();
                Navigator.of(context).push(
                  MaterialPageRoute(
                    builder: (context) => SentencePatternPracticePage(studySentencePatterns: studySentencePatterns),
                  )
                );
              }),
              _card(context, '词义辨析', (){}),
            ],
          ),
        ),
      ),
    );

  Widget _card(BuildContext context, String title, Function onPressed) =>
    Container(
      padding: EdgeInsets.fromLTRB(6, 6, 6, 6),
      alignment: Alignment.center,
      height: 160,
      width: 160,
      decoration: BoxDecoration(
        color: Colors.white,
        borderRadius: BorderRadius.all(Radius.circular(8)),
        /*boxShadow: [
          BoxShadow(color: Colors.black26, offset: Offset(5.0, 5.0), blurRadius: 5.0, spreadRadius: 1.0),
          BoxShadow(color: Colors.black26, offset: Offset(1.0, 1.0)), BoxShadow(color: Colors.black26)
        ],*/
      ),
      child: InkWell(
        child: Text(title, style: TextStyle(fontSize: 17),),
        onTap: onPressed,
      ),
    );
}
